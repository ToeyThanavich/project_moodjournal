# journal/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'journal_entries'
        verbose_name = 'Journal Entry'
        verbose_name_plural = 'Journal Entries'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"

class SentimentAnalysis(models.Model):
    SENTIMENT_CHOICES = [
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    ]
    
    entry = models.OneToOneField(JournalEntry, on_delete=models.CASCADE, related_name='sentiment')
    sentiment_score = models.DecimalField(max_digits=5, decimal_places=4, help_text="Score from -1 to 1")
    sentiment_label = models.CharField(max_length=20, choices=SENTIMENT_CHOICES)
    confidence = models.DecimalField(max_digits=5, decimal_places=4, help_text="0 to 1")
    analyzed_at = models.DateTimeField(auto_now_add=True)
    raw_response = models.JSONField(null=True, blank=True)
    
    class Meta:
        db_table = 'sentiment_analysis'
        verbose_name = 'Sentiment Analysis'
        verbose_name_plural = 'Sentiment Analyses'
    
    def __str__(self):
        return f"{self.entry.id} - {self.sentiment_label}"

class MoodSuggestion(models.Model):
    entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='suggestions')
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'mood_suggestions'
        verbose_name = 'Mood Suggestion'
        verbose_name_plural = 'Mood Suggestions'
    
    def __str__(self):
        return f"Suggestion for {self.entry.id}"